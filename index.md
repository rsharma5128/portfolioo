---
layout: post 
title: Portfolio Home 
hide: true
show_reading_time: false
---

Hi! My name is Rohan Sharma.

## About me

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Glowing Button</title>
  <style>
    body {
      margin: 0;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #0d0d0d;
      font-family: system-ui, sans-serif;
    }

    @keyframes pulse {
      0%, 100% { box-shadow: 0 0 18px 6px #a78bfa, 0 0 40px 12px #7c3aed55; }
      50%       { box-shadow: 0 0 28px 10px #c4b5fd, 0 0 60px 20px #7c3aed88; }
    }

    @keyframes textglow {
      0%, 100% { text-shadow: 0 0 8px #e9d5ff, 0 0 20px #c084fc, 0 0 40px #a855f7; }
      50%       { text-shadow: 0 0 14px #f3e8ff, 0 0 30px #e879f9, 0 0 60px #c026d3; }
    }

    .glow-btn {
      display: inline-block;
      padding: 18px 48px;
      border-radius: 999px;
      background: #1a0a2e;
      border: 1.5px solid #7c3aed;
      color: #fff;
      font-size: 18px;
      font-weight: 500;
      letter-spacing: 0.04em;
      text-decoration: none;
      cursor: pointer;
      animation: pulse 2.8s ease-in-out infinite,
                 textglow 2.8s ease-in-out infinite;
      transition: transform 0.15s;
    }

    .glow-btn:hover  { transform: scale(1.04); }
    .glow-btn:active { transform: scale(0.97); }
  </style>
</head>
<body>
  <a href="https://rsharma5128.github.io/portfolio/about/" class="glow-btn">Here's a little bit about me!</a>
</body>
</html>

## Here are some of the lessons that I have made and curated!



<div style="display: flex; flex-wrap: wrap; gap: 10px;">
    <a href="{{site.baseurl}}/cs111-objectives" style="text-decoration: none;">
        <div style="background-color: var(--green); color: black; padding: 10px 20px; border-radius: 5px; font-weight: bold; transition: transform 0.2s, box-shadow 0.2s;">
           CS111 objectives
        </div>
    </a>
</div>