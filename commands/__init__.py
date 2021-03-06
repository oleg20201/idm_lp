from commands import aliases
from commands import aliases_manager
from commands import delete_messages
from commands import delete_notify
from commands import duty_signal
from commands import info
from commands import members_manager
from commands import ping
from commands import prefixes
from commands import role_play_commands
from commands import run_eval
from commands import self_signal
from commands import set_secret_code

commands_bp = (
    aliases.user,
    aliases_manager.user,
    delete_messages.user,
    delete_notify.user,
    duty_signal.user,
    run_eval.user,
    ping.user,
    info.user,
    prefixes.user,
    role_play_commands.user,
    self_signal.user,
    set_secret_code.user,

    *members_manager.users_bp,
)
