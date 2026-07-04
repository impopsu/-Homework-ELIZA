# ELIZA Chatbot (Homework)

โปรแกรมจำลอง ELIZA แชทบอทที่เลียนแบบนักจิตบำบัดแนว Rogerian
(แนวคิดต้นฉบับโดย Joseph Weizenbaum, 1966) โดยใช้ **regular expression
(regex)** จับรูปแบบประโยคที่ผู้ใช้พิมพ์เข้ามา แล้วสร้างคำตอบกลับไปตาม
กฎที่กำหนดไว้ ทำให้พูดคุยโต้ตอบไปเรื่อยๆ ได้เหมือนแชทบอทจริง

## วิธีการทำงาน

โปรแกรมรับข้อความจากผู้ใช้ทีละบรรทัด แล้ววนตรวจสอบ regex pattern ทีละ
กฎตามลำดับในลิสต์ `RULES` เมื่อเจอ pattern แรกที่ match จะหยุดค้นหา
ทันที และสุ่มเลือกคำตอบหนึ่งข้อความจากชุดคำตอบที่กำหนดไว้ให้กับกฎนั้น

ถ้าประโยคมีการจับกลุ่มคำ (capture group) เช่น `my (.+)` หรือ `i feel (.+)`
โปรแกรมจะทำ **reflection** คือสลับสรรพนามบุรุษที่ 1 กับบุรุษที่ 2 ก่อน
นำไปแทนในคำตอบ เช่น

```
my mother never understood me
   |                       |
  my -> your             me -> you
```

ถ้าไม่มีกฎใด match เลย โปรแกรมจะสุ่มตอบด้วยประโยคทั่วไป (default
response) เช่น "Please tell me more." เพื่อให้บทสนทนาดำเนินต่อไปได้
เรื่อยๆ โดยไม่ค้าง

### หมวดกฎที่มีอยู่ (บางส่วน)

| ตัวกระตุ้น (keyword / pattern)      | แนวคำตอบ                                       |
|--------------------------------------|--------------------------------------------------|
| hello / hi / hey                     | ทักทายกลับ                                       |
| computer(s)                          | ถามความรู้สึกเกี่ยวกับคอมพิวเตอร์                 |
| sorry                                 | บอกว่าไม่ต้องขอโทษ                                |
| i remember X / do you remember X     | ถามย้อนเกี่ยวกับความทรงจำนั้น                     |
| i dream about X                      | ถามเกี่ยวกับความฝัน                              |
| mother/father/sister/brother/family  | ชวนคุยเรื่องครอบครัว                             |
| i'm / i am depressed, sad, unhappy   | แสดงความเห็นใจ หรือถามว่าเป็นแบบนี้นานแค่ไหน       |
| i feel X                              | ถามว่ารู้สึกแบบนี้บ่อยแค่ไหน / อะไรทำให้รู้สึกแบบนี้ |
| i can't X                             | ถามว่ารู้ได้อย่างไรว่าทำไม่ได้                    |
| i need X                              | ถามว่าถ้าได้ X มาจะรู้สึกอย่างไร                  |
| because X                             | ถามว่าเป็นเหตุผลจริงหรือไม่                       |
| are you X                             | สะท้อนคำถามกลับ                                  |
| friend                                | ชวนคุยเรื่องเพื่อน                               |
| yes / no                              | ตอบสนองสั้นๆ ตามน้ำเสียง                         |
| all / always                          | ถามหาตัวอย่างที่เจาะจง                           |
| my X                                  | สะท้อนกลับเป็น "your X" พร้อมถามต่อ                |
| i X (ทั่วไป)                          | สะท้อนกลับเป็นคำถาม                              |
| ประโยคคำถาม (what/how/why/ลงท้าย ?)  | ถามกลับ หรือให้คิดเอง                            |
| ไม่ตรงกฎใดเลย                        | สุ่มตอบทั่วไป เช่น "Please tell me more."         |

พิมพ์ `bye`, `quit` หรือ `exit` เพื่อจบการสนทนา

## ความต้องการของระบบ (Requirements)

- Python 3.x (ทดสอบกับ Python 3.10+)
- ไม่ต้องติดตั้งไลบรารีเพิ่มเติม (ใช้แค่ `re` และ `random` ที่มากับ
  Python อยู่แล้ว)

## วิธีรัน

1. เปิด terminal / command prompt
2. เข้าไปที่โฟลเดอร์ที่มีไฟล์ `eliza.py`
3. รันคำสั่ง

   ```bash
   python3 eliza.py
   ```

   (บน Windows อาจใช้ `python eliza.py` แทน)

4. พิมพ์ประโยคคุยกับ ELIZA แล้วกด Enter โปรแกรมจะตอบกลับทุกครั้ง
5. พิมพ์ `bye`, `quit` หรือ `exit` เพื่อออกจากโปรแกรม

## ตัวอย่างการรัน

```
$ python3 eliza.py
Hello, I am ELIZA. How are you feeling today?
> My mother never understood me.
Tell me more about your family.
> I feel anxious about my exam.
What makes you feel anxious about your exam?
> Because I did not study enough.
Does that reason satisfy you?
> bye
Goodbye. Take care of yourself.
```

คำตอบแต่ละครั้งอาจไม่เหมือนเดิมทุกครั้ง เพราะโปรแกรมสุ่มเลือกจาก
ชุดคำตอบที่เป็นไปได้หลายแบบในแต่ละกฎ
