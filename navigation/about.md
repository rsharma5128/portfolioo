---
layout: post
title: About
permalink: /about/
comments: true
---

<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <a href="https://rsharma5128.opencodingsociety.com/" style="text-decoration: none;">
    <div style="
      display: inline-block;
      padding: 10px 20px;
      border-radius: 999px;
      background: #1a0a2e;
      border: 1.5px solid #7c3aed;
      color: #fff;
      font-weight: bold;
      font-family: system-ui, sans-serif;
      cursor: pointer;
      animation: pulse 2.8s ease-in-out infinite, textglow 2.8s ease-in-out infinite;
      transition: transform 0.15s;
    ">
      🔗 Link back to the homepage
    </div>
  </a>
</div>

<style>
  @keyframes pulse {
    0%, 100% { box-shadow: 0 0 18px 6px #a78bfa, 0 0 40px 12px #7c3aed55; }
    50%       { box-shadow: 0 0 28px 10px #c4b5fd, 0 0 60px 20px #7c3aed88; }
  }
  @keyframes textglow {
    0%, 100% { text-shadow: 0 0 8px #e9d5ff, 0 0 20px #c084fc, 0 0 40px #a855f7; }
    50%       { text-shadow: 0 0 14px #f3e8ff, 0 0 30px #e879f9, 0 0 60px #c026d3; }
  }
</style>

## Where I have been

Here are some places I have lived.

<comment>
Flags are made using Wikipedia images
</comment>

<style>
    /* Style looks pretty compact, 
       - grid-container and grid-item are referenced the code 
    */
    .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); /* Dynamic columns */
        gap: 10px;
    }
    .grid-item {
        text-align: center;
    }
    .grid-item img {
        width: 100%;
        height: 100px; /* Fixed height for uniformity */
        object-fit: contain; /* Ensure the image fits within the fixed height */
    }
    .grid-item p {
        margin: 5px 0; /* Add some margin for spacing */
    }

    .image-gallery {
        display: flex;
        flex-wrap: nowrap;
        overflow-x: auto;
        gap: 10px;
        }

    .image-gallery img {
        max-height: 150px;
        object-fit: cover;
        border-radius: 5px;
    }
</style>

<!-- This grid_container class is used by CSS styling and the id is used by JavaScript connection -->
<div class="grid-container" id="grid_container">
    <!-- content will be added here by JavaScript -->
</div>

<script>
    // 1. Make a connection to the HTML container defined in the HTML div
    var container = document.getElementById("grid_container"); // This container connects to the HTML div

    // 2. Define a JavaScript object for our http source and our data rows for the Living in the World grid
    var http_source = "https://upload.wikimedia.org/wikipedia/commons/";

    var living_in_the_world = [
        {flag: "0/01/Flag_of_California.svg", greeting: "Hello!", description: "California - all my life!!!"}, {flag: "8/88/Flag_of_India_%282-1%29.svg", greeting: "Namaste Beta", description: "India - where my parents are from"}

    ];

    // 3a. Consider how to update style count for size of container
    // The grid-template-columns has been defined as dynamic with auto-fill and minmax

    // 3b. Build grid items inside of our container for each row of data
    for (const location of living_in_the_world) {
        // Create a "div" with "class grid-item" for each row
        var gridItem = document.createElement("div");
        gridItem.className = "grid-item";  // This class name connects the gridItem to the CSS style elements
        // Add "img" HTML tag for the flag
        var img = document.createElement("img");
        img.src = http_source + location.flag; // concatenate the source and flag
        img.alt = location.flag + " Flag"; // add alt text for accessibility

        // Add "p" HTML tag for the description
        var description = document.createElement("p");
        description.textContent = location.description; // extract the description

        // Add "p" HTML tag for the greeting
        var greeting = document.createElement("p");
        greeting.textContent = location.greeting;  // extract the greeting

        // Append img and p HTML tags to the grid item DIV
        gridItem.appendChild(img);
        gridItem.appendChild(description);
        gridItem.appendChild(greeting);

        // Append the grid item DIV to the container DIV
        container.appendChild(gridItem);
    }
</script>

### Journey through Life

Here is where life has taken me!

**School**

- 🏫 Deer Canyon Elementary School(2015-2016)

- 🏫 Stone Ranch Elementary School(2016-2022)

- 🏫 Oak Valley Middle School(2022-2025)

- 🏫 Del Norte High School(Freshman year, 2025-Present)

**Extracurricular**

🛡️ 1 year of CyberPatriot

🎵 Traditional Indian vocal music since I was 5 years old

🎾 Used to play tennis

🏃 Started Cross Country this year

🥍 Currently in Lacrosse pre-season

💻 Helped my friend Matt with game developing in Roblox Studio

## Photo Gallery of my Interests

<div class="grid-container" id="roblox_grid"></div>


<script>
   var robloxContainer = document.getElementById("roblox_grid");
  
   var projects = [
       {
           image: "https://upload.wikimedia.org/wikipedia/commons/5/52/YouTube_social_white_circle_%282017%29.svg",
           title: "YouTube",
           description: "I enjoy watching videos about hardware and cars on YouTube, as those are 2 fields which interest me. I enjoy watching YouTubers such as Garbage Time, Psivewri, and Salem Techsperts."
       },
       {
           image: "https://upload.wikimedia.org/wikipedia/commons/4/48/Roblox_Logo_2021.png",
           title: "Roblox",
           description: "I enjoy playing games on Roblox in my free time, and I play games such as Jailbreak, Infamy and Arcane Odyssey with my friend Kyle and games like Riotfall by myself."
       },
       {
           image: "https://upload.wikimedia.org/wikipedia/commons/f/f9/Initial_D_Logo.png",
           title: "Initial D",
           description: "Initial D was an anime which aired from 1998 to 2010. It is an anime about an 18 year old teenager delivering tofu in mountain passes late at night and how he gets exposed to the world of illegal street racing. I enjoy watching this anime because of the techniques used which also relate to properties of physics."
       },
       {
        image: "https://upload.wikimedia.org/wikipedia/commons/8/8e/IFixit_logo.svg",
        title: "Computer Repair",
        description: "In my free time, I occasionally enjoy repairing computers. It is stressful at times, but I find pleasure in doing things like reapplying thermal paste and fixing broken computers to a state of working again. I chose the IFixit logo to represent this as the guides on there have helped me a lot with some of the repairs that I do."
       }
   ];


   for (const project of projects) {
       var gridItem = document.createElement("div");
       gridItem.className = "grid-item";


       var img = document.createElement("img");
       img.src = project.image;
       img.alt = project.title;


       var title = document.createElement("p");
       title.textContent = project.title;


       var description = document.createElement("p");
       description.textContent = project.description;


       gridItem.appendChild(img);
       gridItem.appendChild(title);
       gridItem.appendChild(description);
       robloxContainer.appendChild(gridItem);
   }
</script>



### Background

My family is my main inspiration, and they are the reason I am still here today and in this CS class!

👩🏻 1 older sister in college

🇮🇳 Both parents from India, more specifically southern region, with my dad being from Karnataka and my mom being from Tamil Nadu

👨‍👩‍👦 My cousins are more on my dad's side, and a lot of them live in India, but 2 of them live in the US and one of them lives in the UK

<comment>
Gallery of Pics...
</comment>
<div class="image-gallery">
  <img src="{{site.baseurl}}/images/about/mort2.jpg" alt="Image 2">
  <img src="{{site.baseurl}}/images/about/mort4.jpg" alt="Image 3">
  <img src="{{site.baseurl}}/images/about/mort5.jpg" alt="Image 3">
</div>