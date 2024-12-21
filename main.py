import re
from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *
# 注册插件
@register(name="dev", description="插件测试", version="0.1", author="bright")
class MyPlugin(BasePlugin):

    # 插件加载时触发
    def __init__(self, host: APIHost):
        self.host = host

    # 异步初始化
    async def initialize(self):
        pass

    # 插件卸载时触发
    def __del__(self):
        pass

    @handler(NormalMessageResponded)
    async def on_normal_message_responded(self, ctx: EventContext):
        await ctx.send_message("[bot] 插件测试")
