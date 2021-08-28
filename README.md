<div dir="rtl">
<h1>
طرح پیشنهادی
</h1>

در این ریپازیتوری تمام ایده ها و پیشنهادات اعضاء برای بات تلگرام را جمع آور خواهیم کرد. لطفا از زبان مارک داون و اچ تی ام ال برای نوشتن و لیست کردن ایده ها استفاده کنید.

تلاش بر این خواهد بود که یک بات متن باز تلگرام برای گروه تبادل ارز هلند ساخته شود و از زبان برنامه نویسی پایتون برای این منظور استفاده خواهد شد.

<h2>
ایده ها
</h2>
 
<ul>
  <li>
    هر عضو جدید وارد گروه توسط ربات خوش آمد گویی شده و قوانین و نمات ایمنی را به صورت خصوصی دریافت کند
  </li>
  <li>
    تاریخ ساخته شدن اکانت تلگرام هر عضو جدید و زمان آپلود شدن عکس های وی بررسی شود و احتمال کلاهبردار بودن به ادمین ها ریپورت شود
  </li>
</ul>
</div>


## Run the bot

1. Clone the project:
    ```bash
    git clone https://github.com/tabadolArzNL/proposal.git
    cd proposal
    ```

2. Install the requirements:
    ```bash
    pip install -r requirements.txt
    ```

3. Add environments variables:

    create a file call `.env`:
    ```bash
    touch .env
    ```

    and add this variables to it:
    ```env
    TOKEN=your-telegram-bot-token
    ```

4. run the app:

    ```bash
    python main.py
    ```