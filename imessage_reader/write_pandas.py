import pandas as pd

class DataFrameWriter:
    """This class manages the export to a Pandas DataFrame."""

    def __init__(self, imessage_data: list):
        """
        Constructor method

        :param imessage_data: list with MessageData objects
                containing user id, text, date, service and account
        """
        self.imessage_data = imessage_data

    def to_dataframe(self) -> pd.DataFrame:
        """
        Convert data to a Pandas DataFrame.

        :return: A Pandas DataFrame containing the iMessage data
        """
        users = []
        messages = []
        dates = []
        services = []
        accounts = []
        is_from_me = []

        for data in self.imessage_data:
            users.append(data.user_id)
            messages.append(data.text)
            dates.append(data.date)
            services.append(data.service)
            accounts.append(data.account)
            is_from_me.append(data.is_from_me)

        # Create a DataFrame
        df = pd.DataFrame({
            'User ID': users,
            'Message': messages,
            'Date': dates,
            'Service': services,
            'Account': accounts,
            'Is From Me': is_from_me
        })

        return df

# Example usage:
# imessage_data = [MessageData(...), MessageData(...), ...]  # List of MessageData objects
# writer = DataFrameWriter(imessage_data)
# df = writer.to_dataframe()
# print(df)
