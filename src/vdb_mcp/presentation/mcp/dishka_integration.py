from inspect import Parameter
from typing import Any, TypeVar, ParamSpec, Callable, get_type_hints

from dishka import AsyncContainer, Scope
from dishka.integrations.base import wrap_injection
from fastmcp import FastMCP, Context
from fastmcp.server.middleware import Middleware, MiddlewareContext, CallNext
from mcp import types as mt

T = TypeVar("T")
P = ParamSpec("P")

_ContainerCtxKey = "dishka_container"
_DISHKA_CONTEXT_PARAM = Parameter(
    name="___dishka_request",
    annotation=MiddlewareContext,
    kind=Parameter.KEYWORD_ONLY,
)


def setup_dishka(
    container: AsyncContainer,
    app: FastMCP,
) -> None:
    """Setup dishka integration for FastMCP app."""
    app.add_middleware(_ContainerMiddleware())
    app.dishka_container = container


def inject(func: Callable[P, T]) -> Callable[P, T]:
    """Inject dishka dependencies into tool."""
    return _wrap_fastmcp_injection(func=func)


class _ContainerMiddleware(Middleware):
    """Dishka middleware for FastMCP app."""

    async def on_request(
        self,
        context: MiddlewareContext[mt.Request[Any, Any]],
        call_next: CallNext[mt.Request[Any, Any], Any],
    ) -> Any:
        """Inject request container into context."""
        ctx = context.fastmcp_context

        async with ctx.fastmcp.dishka_container(scope=Scope.REQUEST) as req_container:
            ctx.set_state(
                _ContainerCtxKey,
                req_container,
            )

        injected_context = context.copy(fastmcp_context=ctx)

        return await call_next(injected_context)


def _wrap_fastmcp_injection(
    *,
    func: Callable[P, T],
) -> Callable[P, T]:
    """Wrap injection for usage with FastMCP."""
    param_name = _find_context_param(func)
    if param_name:
        additional_params = []
    else:
        additional_params = [_DISHKA_CONTEXT_PARAM]
        param_name = _DISHKA_CONTEXT_PARAM.name

    return wrap_injection(
        func=func,
        is_async=True,
        additional_params=additional_params,
        container_getter=lambda _, p: p[param_name].get_state(_ContainerCtxKey),
    )


def _find_context_param(func: Callable[P, T]) -> str | None:
    """Find Context parameter name in tool definition."""
    hints = get_type_hints(func)

    return next(
        (name for name, hint in hints.items() if hint is Context),
        None,
    )
