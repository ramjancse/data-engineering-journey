# Class 02 --- Linux Commands Reference

**Ostad Data Engineering Bootcamp --- Batch 01**

এই ফাইলে ক্লাসে শেখানো Linux command-গুলো বিষয় অনুযায়ী সাজিয়ে রাখা হয়েছে।

------------------------------------------------------------------------

## 1. Directory Navigation --- ফোল্ডার নেভিগেশন

  Command          কাজ
  ---------------- ------------------------------------------------
  `pwd`            বর্তমানে কোন directory-তে আছি তা দেখায়
  `ls`             ফাইল ও ফোল্ডারের তালিকা দেখায়
  `ls -lh`         বিস্তারিত তথ্য ও human-readable file size দেখায়
  `ls -lhS`        বড় ফাইল আগে দেখায়
  `cd folder`      নির্দিষ্ট folder-এ প্রবেশ করে
  `cd ..`          এক ধাপ উপরের directory-তে যায়
  `cd ~`           Home directory-তে যায়
  `cd -`           আগের directory-তে ফিরে যায়
  `mkdir -p a/b`   প্রয়োজন হলে parent directory-সহ folder তৈরি করে

**উদাহরণ:**

``` bash
pwd
ls -lh
cd Documents
cd ..
mkdir -p projects/data-engineering
```

## 2. File Management --- ফাইল ব্যবস্থাপনা

  Command                      কাজ
  ---------------------------- ---------------------------------
  `cp a b`                     ফাইল `a` কপি করে `b` নামে রাখে
  `cp -r source destination`   directory-সহ recursive copy করে
  `mv old new`                 ফাইল/ফোল্ডার move বা rename করে
  `rm file`                    ফাইল স্থায়ীভাবে মুছে ফেলে
  `rm -r folder`               folder ও তার contents মুছে ফেলে

> **সতর্কতা:** `rm` দিয়ে মুছে ফেলা ফাইল সাধারণত Recycle Bin-এ যায় না।
> command চালানোর আগে path ভালোভাবে যাচাই করুন।

## 3. Reading Files --- ফাইল পড়া

  Command              কাজ
  -------------------- ---------------------------------
  `head -5 file.txt`   ফাইলের প্রথম ৫ লাইন দেখায়
  `tail -5 file.txt`   ফাইলের শেষ ৫ লাইন দেখায়
  `tail -f app.log`    log file-এর নতুন লাইন live দেখায়
  `wc -l file.txt`     মোট line সংখ্যা গণনা করে
  `less file.txt`      page ধরে ফাইল পড়তে দেয়
  `cat file.txt`       পুরো ফাইল terminal-এ দেখায়

> বড় ফাইলের ক্ষেত্রে `cat` ব্যবহার না করে `less`, `head`, বা `tail` ব্যবহার
> করা ভালো।

## 4. grep --- টেক্সট খোঁজা

  Command                        কাজ
  ------------------------------ --------------------------------------
  `grep "ERROR" app.log`         `ERROR` লেখা line খোঁজে
  `grep -c "ERROR" app.log`      কতটি line-এ `ERROR` আছে গণনা করে
  `grep -i "error" app.log`      বড়/ছোট হাতের অক্ষর উপেক্ষা করে
  `grep -v "INFO" app.log`       `INFO` নেই এমন line দেখায়
  `grep -n "ERROR" app.log`      line number-সহ ফলাফল দেখায়
  `grep "^2026-10-17" app.log`   নির্দিষ্ট তারিখ দিয়ে শুরু হওয়া line খোঁজে
  `grep -r "ERROR" folder/`      folder-এর ভেতরে recursive search করে

## 5. cut, sort, uniq, tr --- ডেটা থেকে অংশ বের করা ও সাজানো

  Command                    কাজ
  -------------------------- ------------------------------------------
  `cut -c1-10 file.txt`      প্রতিটি line-এর প্রথম ১০টি character দেখায়
  `cut -d',' -f3 file.csv`   comma-delimited ফাইলের ৩য় field বের করে
  `cut -d'|' -f2 file.txt`   pipe-delimited ফাইলের ২য় field বের করে
  `sort file.txt`            line alphabetically সাজায়
  `sort -rn file.txt`        সংখ্যাকে descending order-এ সাজায়
  `uniq -c`                  পরপর থাকা duplicate line গণনা করে
  `tr -d ' '`                space character মুছে ফেলে

**মনে রাখুন:** `uniq` সাধারণত পাশাপাশি থাকা duplicate line একসঙ্গে গণনা
করে। তাই আগে `sort` করা হয়।

**উদাহরণ:**

``` bash
sort names.txt | uniq -c
```

## 6. Pipes and Redirection --- command একসঙ্গে ব্যবহার

Pipe (`|`) দিয়ে একটি command-এর output পরের command-এর input হিসেবে
পাঠানো যায়।

``` bash
grep "| ERROR |" app.log | cut -c1-10 | sort | uniq -c | sort -rn
```

  -----------------------------------------------------------------------
  Operator                            কাজ
  ----------------------------------- -----------------------------------
  `command1 \| command2`              প্রথম command-এর output দ্বিতীয়
                                      command-এ পাঠায়

  `>`                                 ফাইলে output লেখে; আগের content
                                      overwrite করে

  `>>`                                ফাইলের শেষে output যোগ করে
  -----------------------------------------------------------------------

**উদাহরণ:**

``` bash
ls -lh > files.txt
echo "New entry" >> notes.txt
```

## 7. File Permissions --- ফাইলের অনুমতি

  Permission   অর্থ
  ------------ ---------------------------------
  `r`          Read --- পড়ার অনুমতি
  `w`          Write --- লেখার/পরিবর্তনের অনুমতি
  `x`          Execute --- চালানোর অনুমতি

**Commands:**

``` bash
ls -l script.sh
chmod +x script.sh
./script.sh
```

-   `ls -l` দিয়ে permission দেখা যায়।
-   `chmod +x` দিয়ে execute permission যোগ করা হয়।
-   `./script.sh` দিয়ে বর্তমান directory থেকে script চালানো হয়।

## 8. Environment Variables --- পরিবেশ ভেরিয়েবল

  Command                কাজ
  ---------------------- -------------------------------------------
  `echo $HOME`           Home directory দেখায়
  `echo $PATH`           command খোঁজার directory-গুলোর তালিকা দেখায়
  `export API_KEY=abc`   বর্তমান shell session-এ variable সেট করে
  `env \| grep API`      API-সম্পর্কিত environment variable খোঁজে

**সিক্রেট/credentials বিষয়ে সতর্কতা:** - API key বা password সরাসরি Git
repository-তে commit করবেন না। - `.env` ফাইলে secret রাখলে
`.gitignore`-এ `.env` যোগ করুন। - প্রয়োজন হলে নিরাপদ example হিসেবে
`.env.example` রাখুন, কিন্তু আসল secret রাখবেন না।

## 9. Cron --- Scheduled Tasks

  Command        কাজ
  -------------- ----------------------------
  `crontab -e`   cron schedule edit করে
  `crontab -l`   বর্তমান cron schedule দেখায়

Cron schedule-এর সাধারণ format:

``` text
minute hour day-of-month month day-of-week command
```

**উদাহরণ:**

``` cron
0 2 * * * /path/to/backup.sh
```

এটি প্রতিদিন রাত ২টায় script চালানোর schedule।

## 10. অতিরিক্ত সহায়ক Linux Commands

নিচের command-গুলো ক্লাসের মূল তালিকার বাইরে, 
  Command                  কাজ
  ------------------------ -------------------------------------
  `df -h`                  disk space দেখায়
  `du -sh folder/`         folder-এর মোট size দেখায়
  `find . -name "*.csv"`   বর্তমান directory থেকে CSV ফাইল খোঁজে
  `history`                আগে চালানো command-এর history দেখায়
  `clear`                  terminal পরিষ্কার করে

------------------------------------------------------------------------

## Quick Safety Checklist

-   `rm` চালানোর আগে path যাচাই করুন।
-   `>` ফাইলের পুরোনো content overwrite করে; `>>` শেষে যোগ করে।
-   বড় ফাইল দেখতে `cat`-এর বদলে `less`, `head`, বা `tail` ব্যবহার করুন।
-   API key, password, `.env` এবং credentials GitHub-এ commit করবেন না।
-   কোনো command বুঝতে অসুবিধা হলে আগে `man command` অথবা `command --help`
    দেখে নিন।


