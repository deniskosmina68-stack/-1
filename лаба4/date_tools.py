from datetime import datetime
import humanize

def show_date():
    now = datetime.now()
    print("\nПоточна дата:", now.strftime("%d.%m.%Y %H:%M"))
    print("Відносний час:", humanize.naturaltime(now))
