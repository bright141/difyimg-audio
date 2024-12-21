import re
from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext

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
    async def text_to_voice(self, ctx: EventContext):
        user_prefer = self.ncv.load_user_preference(ctx.event.sender_id)
        if not user_prefer["voice_switch"]:
            return
