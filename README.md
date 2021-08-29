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

    Create a file call `.env`:
    ```bash
    touch .env
    ```

    And add this variables to it:
    ```env
    TOKEN=your-telegram-bot-token
    ```

4. Run the app:

    ```bash
    python main.py
    ```

### Run the project for development
- To reload the project after changing the code, we can use `nodemon`
     ```bash
     npm install -g nodemon
     ```

- And now we can use the `nodemon`
    ```bash
    nodemon main.py
    ```


### The telegram library we use
we will use `python-telegram-bot` for our telegram bot:
- https://github.com/python-telegram-bot/python-telegram-bot

you can see the documentation of the library here:
- https://python-telegram-bot.readthedocs.io/en/stable/

also some examples for `python-telegram-bot`:
https://github.com/python-telegram-bot/python-telegram-bot/tree/master/examples

