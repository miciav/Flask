class NotificationManager:
    last_id: int = 0

    def __init__(self):
        self.notifications = {}

    def insert_notification(self, notification):
        # this is not thread-safe
        self.__class__.last_id += 1
        notification.id = self.__class__.last_id
        self.notifications[self.__class__.last_id] = notification

    def get_notification(self, id):
        return self.notifications[id]

    def delete_notification(self, id):
        del self.notifications[id]
