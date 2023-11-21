import asyncio

import telegram

token = "your_token_key"
chat_id = "your_chat_id"


async def report_message(notification_message: str) -> None:
    """
    Sends a notification message to a Telegram group.

    Args:
    - notification_message (str): The notification message to be reported.

    Returns:
    - None
    """
    bot = telegram.Bot(token=token)

    await bot.sendMessage(chat_id=chat_id, text=notification_message)

    print("Notification reported to the telegram group!")


if __name__ == '__main__':
    # Example Usage
    try:
        result = 5 / 0
        print(result)
    except ZeroDivisionError as e:
        error_text = f"Error: {str(e)}"
        asyncio.run(report_message(notification_message=error_text))
