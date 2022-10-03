import html
import random
import YinsRobot.modules.truth_and_dare_string as truth_and_dare_string
from YinsRobot import dispatcher
from telegram import ParseMode, Update, Bot
from YinsRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async


def truth(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.TRUTH))


def dare(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.DARE))
    
def acak(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.ACAK))

def helps(chat):
    return gs(chat, "truthordare_help")

ACAK_HANDLER = DisableAbleCommandHandler("acak", acak, run_async=True)
TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth, run_async=True)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare, run_async=True)

dispatcher.add_handler(ACAK_HANDLER)
dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)
