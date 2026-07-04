# ELIZA Chatbot (Homework)

โปรแกรมจำลอง ELIZA แชทบอทยุคแรกที่เลียนแบบนักจิตบำบัดแนว Rogerian
(Joseph Weizenbaum, 1966) โดยใช้ **regular expression (regex)** จับรูปแบบ
ประโยคที่ผู้ใช้พิมพ์เข้ามา แล้วสร้างคำตอบกลับไปตามกฎที่กำหนดไว้

อ้างอิงจากสไลด์การเรียน หน้า 80–82 (Simple Application: ELIZA / How ELIZA works)

## วิธีการทำงาน

โปรแกรมจะรับข้อความจากผู้ใช้ทีละบรรทัด แล้ววนตรวจสอบ regex pattern ทีละกฎ
ตามลำดับในลิสต์ `RULES` เมื่อเจอ pattern แรกที่ match จะหยุดค้นหาทันที
และสร้างคำตอบจากเทมเพลตของกฎนั้น

ถ้าประโยคมีการจับกลุ่มคำ (capture group) เช่น `my (.+)` โปรแกรมจะทำ
**reflection** คือสลับสรรพนามบุรุษที่ 1 กับบุรุษที่ 2 ก่อนนำไปแทนใน
คำตอบ เช่น

```
my boyfriend made me come here
        |              |
       my -> your      me -> you
        v
your boyfriend made you come here
```

ถ้าไม่มีกฎใด match เลย โปรแกรมจะสุ่มตอบด้วยประโยคทั่วไป (default response)
เช่น "PLEASE TELL ME MORE." เพื่อให้บทสนทนาดำเนินต่อไปได้เรื่อยๆ

### ตารางกฎ (บางส่วน)

| Pattern (regex)              | ตัวอย่างคำตอบ                                  |
|-------------------------------|------------------------------------------------|
| `i'm (depressed\|sad)`        | I AM SORRY TO HEAR YOU ARE ...                 |
| `i am (depressed\|sad)`       | WHY DO YOU THINK YOU ARE ...                   |
| `i need (.+)`                 | WHAT WOULD IT MEAN TO YOU IF YOU GOT ...?      |
| `all`                          | IN WHAT WAY?                                   |
| `always`                       | CAN YOU THINK OF A SPECIFIC EXAMPLE?           |
| `my (.+)`                      | YOUR ... (พร้อมสลับสรรพนาม)                     |
| `i (.+)`                       | DO YOU REALLY THINK SO? / WHY DO YOU SAY ...   |
| จบด้วย `?`                    | WHY DO YOU ASK THAT? ฯลฯ                       |
| ไม่ตรงกฎใดเลย                 | สุ่มตอบทั่วไป เช่น PLEASE TELL ME MORE.        |

พิมพ์ `bye`, `quit` หรือ `exit` เพื่อจบการสนทนา

## ความต้องการของระบบ (Requirements)

- Python 3.x (ทดสอบกับ Python 3.10+)
- ไม่ต้องติดตั้งไลบรารีเพิ่มเติม (ใช้แค่ `re` และ `random` ที่มากับ Python
  อยู่แล้ว)

## วิธีรัน

1. เปิด terminal / command prompt
2. เข้าไปที่โฟลเดอร์ที่มีไฟล์ `eliza.py`
3. รันคำสั่ง

   ```bash
   python3 eliza.py
   ```

   (บน Windows อาจใช้ `python eliza.py` แทน)

4. พิมพ์ประโยคคุยกับ ELIZA แล้วกด Enter โปรแกรมจะตอบกลับทุกครั้ง
5. พิมพ์ `bye` เพื่อออกจากโปรแกรม

## ตัวอย่างการรัน

```
$ python3 eliza.py
HELLO, I AM ELIZA. HOW ARE YOU FEELING TODAY?
> Men are all alike.
IN WHAT WAY?
> They're always bugging us about something or other.
CAN YOU THINK OF A SPECIFIC EXAMPLE?
> Well, my boyfriend made me come here.
YOUR BOYFRIEND MADE YOU COME HERE
> He says I'm depressed much of the time.
I AM SORRY TO HEAR YOU ARE DEPRESSED
> bye
GOODBYE. TAKE CARE OF YOURSELF.
```

ผลลัพธ์ตรงกับตัวอย่างบทสนทนาในสไลด์หน้า 81 ทุกบรรทัด
