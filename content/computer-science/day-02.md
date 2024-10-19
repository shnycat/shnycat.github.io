+++
title = 'Day 02'
date = 2024-10-19T05:36:59Z
+++
### Day 2: Binary Systems and Data Representation

#### Introduction to Binary Systems

Computers operate using binary numbers because their hardware is based on electrical signals that have two states: **on** or **off**. These states are represented by **1** (on) and **0** (off). This is the foundation of the binary system, also called **base-2**.

#### Decimal vs. Binary

You’re familiar with the **decimal system** (base-10), which uses ten digits (0-9). The binary system works similarly, but instead of ten digits, it uses only two digits (0 and 1).

##### Example:
- Decimal number **9** is written as **1001** in binary:
   - $9_{10} = 1 \times 2^3 + 0 \times 2^2 + 0 \times 2^1 + 1 \times 2^0$

In binary, each digit (bit) represents a power of 2, starting from the right. So, binary **1001** equals $1 \times 8 + 0 \times 4 + 0 \times 2 + 1 \times 1 = 9$.

#### Converting Decimal to Binary

To convert a decimal number to binary:
1. Divide the number by 2.
2. Record the remainder (either 0 or 1).
3. Repeat the division until you reach 0.
4. The binary representation is the sequence of remainders read from bottom to top.

##### Example:
Convert **13** to binary:
1. $13 / 2 = 6$ remainder **1**
2. $6 / 2 = 3$ remainder **0**
3. $3 / 2 = 1$ remainder **1**
4. $1 / 2 = 0$ remainder **1**

So, **13** in decimal is **1101** in binary.

#### Hexadecimal System (Base-16)

Binary can get long and complex, so programmers often use the **hexadecimal system** (base-16) as a shorthand. Hex uses 16 digits: 0-9 and the letters A-F (representing 10-15).

##### Example:
- The decimal number **255** is written as **FF** in hexadecimal:
  - $255_{10} = 15 \times 16^1 + 15 \times 16^0$

Hexadecimal simplifies reading large binary numbers because one hex digit represents four binary digits.

#### How Computers Represent Data

1. **Text**: Text is represented using binary codes, with each letter or symbol mapped to a specific sequence of bits. The most common standard is **ASCII** (American Standard Code for Information Interchange), where each character is assigned a number:
   - Example: The letter ‘A’ is represented as **65** in decimal or **01000001** in binary.

2. **Images**: Digital images are made of pixels, and each pixel’s color is represented by binary values. In the simplest case, a black-and-white image uses 1 bit per pixel (0 for black, 1 for white). In colored images, each pixel uses a combination of binary numbers to represent shades of red, green, and blue.

3. **Sound**: Sound is captured as a series of samples (discrete points in time) and converted to binary. A common format is **MP3**, which compresses the binary data to save space while keeping the quality acceptable.

#### Why Binary?

The binary system is efficient for computers because it aligns perfectly with their hardware:
- **Transistors**: The basic building blocks of modern computers are transistors, which are either in an "on" (1) or "off" (0) state. This makes binary the natural choice for data representation.
- **Logic Gates**: The fundamental operations computers perform (AND, OR, NOT) are easy to implement with binary logic.

#### Tasks for Today:
1. **Convert a few decimal numbers to binary**. Try converting **10**, **25**, and **50** to binary.
2. **Explore text encoding**: Look up the ASCII codes for a few letters of your name and convert those to binary.
   
#### Summary:
- Computers use the binary system to represent all types of data.
- Binary is based on two digits (0 and 1) and aligns with the on-off states of computer hardware.
- Hexadecimal provides a convenient way to represent large binary numbers.
- Text, images, and sound are all converted to binary for processing by computers.

Tomorrow, we will explore computer architecture and the role of the CPU, memory, and storage.
