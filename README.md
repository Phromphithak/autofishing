<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Autofish for Berlin v2 By XIL</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }

        h1 {
            text-align: center;
        }

        .center {
            display: flex;
            justify-content: center;
            align-items: center;
        }

        img {
            max-width: 100%;
            height: auto;
        }

        .code {
            background-color: #f4f4f4;
            border: 1px solid #ddd;
            border-left: 3px solid #3a87ad;
            color: #666;
            page-break-inside: avoid;
            font-family: monospace;
            font-size: 15px;
            line-height: 1.6;
            margin-bottom: 1.6em;
            padding: 1em;
            display: block;
            overflow: auto;
        }

        .code::-webkit-scrollbar {
            width: 12px;
        }

        .code::-webkit-scrollbar-thumb {
            background-color: #3a87ad;
        }

        .code::-webkit-scrollbar-track {
            background-color: #f4f4f4;
        }

        .code pre {
            margin: 0;
            display: inline-block;
            max-width: 100%;
            overflow: visible;
        }
    </style>
</head>
<body>
    <h1>Autofish for Berlin v2 By XIL</h1>

    <div class="center">
        <img src="autofish_icon.png" alt="Autofish Icon">
    </div>

    <h2>คำอธิบาย</h2>
    <p>โปรเจ็กต์นี้เป็นโปรแกรมที่ถูกพัฒนาโดย XIL และออกแบบมาเพื่อช่วยในกระบวนการตรวจจับสีแดงทับสีเขียวเพื่อให้สามารถทำงานอัตโนมัติ (Autofish) ในเกม Berlin ได้.</p>

    <h2>วิธีใช้</h2>
    <ol>
        <li>เลือกหน้าต่างที่ต้องการจับภาพด้วยการเลือกจากรายการหน้าต่างที่เปิดอยู่.</li>
        <li>คลิกที่ปุ่ม "Start" เพื่อเริ่มต้นกระบวนการตรวจจับ.</li>
        <li>คลิกที่ปุ่ม "Stop" เพื่อหยุดกระบวนการตรวจจับ.</li>
    </ol>

    <h2>ความต้องการระบบ</h2>
    <ul>
        <li>Python 3.x</li>
        <li>OpenCV</li>
        <li>PyQt5</li>
        <li>pygetwindow</li>
        <li>keyboard</li>
        <li>numpy</li>
    </ul>

    <h2>วิธีติดตั้งและการใช้งาน</h2>
    <ol>
        <li>ติดตั้ง Python 3.x จาก <a href="https://www.python.org/downloads/">เว็บไซต์หลักของ Python</a>.</li>
        <li>ติดตั้งไลบรารีที่จำเป็นโดยใช้คำสั่ง <code>pip install opencv-python PyQt5 pygetwindow keyboard numpy</code>.</li>
        <li>เปิดโปรแกรมโดยการรันไฟล์ <code>autofish.py</code> ผ่าน Python.</li>
    </ol>

    <h2>ข้อควรระวัง</h2>
    <ul>
        <li>การใช้โปรแกรมนี้อาจเป็นการละเมิดเงื่อนไขการใช้งานของเกมหรือเป็นการล
