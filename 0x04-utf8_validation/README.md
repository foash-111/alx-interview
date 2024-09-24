# alx-interview
 0x04-utf8_validation

Unicode

Unicode was a brave effort to create a single character set that included every reasonable writing system on the planet and some make-believe ones like Klingon, too. Some people are under the misconception that Unicode is simply a 16-bit code where each character takes 16 bits and therefore there are 65,536 possible characters. This is not, actually, correct. It is the single most common myth about Unicode, so if you thought that, don’t feel bad.



Ever wonder about that mysterious Content-Type tag? You know, the one you’re supposed to put in HTML and you never quite know what it should be?

Did you ever get an email from your friends in Bulgaria with the subject line “???? ?????? ??? ????”?

I’ve been dismayed to discover just how many software developers aren’t really completely up to speed on the mysterious world of character sets, encodings, Unicode, all that stuff. A couple of years ago, a beta tester for FogBUGZ was wondering whether it could handle incoming email in Japanese. Japanese? They have email in Japanese? I had no idea. When I looked closely at the commercial ActiveX control we were using to parse MIME email messages, we discovered it was doing exactly the wrong thing with character sets, so we actually had to write heroic code to undo the wrong conversion it had done and redo it correctly. When I looked into another commercial library, it, too, had a completely broken character code implementation. I corresponded with the developer of that package and he sort of thought they “couldn’t do anything about it.” Like many programmers, he just wished it would all blow over somehow.

But it won’t. When I discovered that the popular web development tool PHP has almost complete ignorance of character encoding issues, blithely using 8 bits for characters, making it darn near impossible to develop good international web applications, I thought, enough is enough.

So I have an announcement to make: if you are a programmer working in 2003 and you don’t know the basics of characters, character sets, encodings, and Unicode, and I catch you, I’m going to punish you by making you peel onions for 6 months in a submarine. I swear I will.

And one more thing:

IT’S NOT THAT HARD.

In this article I’ll fill you in on exactly what every working programmer should know. All that stuff about “plain text = ascii = characters are 8 bits” is not only wrong, it’s hopelessly wrong, and if you’re still programming that way, you’re not much better than a medical doctor who doesn’t believe in germs. Please do not write another line of code until you finish reading this article.

Before I get started, I should warn you that if you are one of those rare people who knows about internationalization, you are going to find my entire discussion a little bit oversimplified. I’m really just trying to set a minimum bar here so that everyone can understand what’s going on and can write code that has a hope of working with text in any language other than the subset of English that doesn’t include words with accents. And I should warn you that character handling is only a tiny portion of what it takes to create software that works internationally, but I can only write about one thing at a time so today it’s character sets.

A Historical Perspective

The easiest way to understand this stuff is to go chronologically.

You probably think I’m going to talk about very old character sets like EBCDIC here. Well, I won’t. EBCDIC is not relevant to your life. We don’t have to go that far back in time.

ASCII tableBack in the semi-olden days, when Unix was being invented and K&R were writing The C Programming Language, everything was very simple. EBCDIC was on its way out. The only characters that mattered were good old unaccented English letters, and we had a code for them called ASCII which was able to represent every character using a number between 32 and 127. Space was 32, the letter “A” was 65, etc. This could conveniently be stored in 7 bits. Most computers in those days were using 8-bit bytes, so not only could you store every possible ASCII character, but you had a whole bit to spare, which, if you were wicked, you could use for your own devious purposes: the dim bulbs at WordStar actually turned on the high bit to indicate the last letter in a word, condemning WordStar to English text only. Codes below 32 were called unprintable and were used for cussing. Just kidding. They were used for control characters, like 7 which made your computer beep and 12 which caused the current page of paper to go flying out of the printer and a new one to be fed in.

And all was good, assuming you were an English speaker.

Because bytes have room for up to eight bits, lots of people got to thinking, “gosh, we can use the codes 128-255 for our own purposes.” The trouble was, lots of people had this idea at the same time, and they had their own ideas of what should go where in the space from 128 to 255. The IBM-PC had something that came to be known as the OEM character set which provided some accented characters for European languages and a bunch of line drawing characters… horizontal bars, vertical bars, horizontal bars with little dingle-dangles dangling off the right side, etc., and you could use these line drawing characters to make spiffy boxes and lines on the screen, which you can still see running on the 8088 computer at your dry cleaners’. In fact  as soon as people started buying PCs outside of America all kinds of different OEM character sets were dreamed up, which all used the top 128 characters for their own purposes. For example on some PCs the character code 130 would display as é, but on computers sold in Israel it was the Hebrew letter Gimel (ג), so when Americans would send their résumés to Israel they would arrive as rגsumגs. In many cases, such as Russian, there were lots of different ideas of what to do with the upper-128 characters, so you couldn’t even reliably interchange Russian documents.

Eventually this OEM free-for-all got codified in the ANSI standard. In the ANSI standard, everybody agreed on what to do below 128, which was pretty much the same as ASCII, but there were lots of different ways to handle the characters from 128 and on up, depending on where you lived. These different systems were called code pages. So for example in Israel DOS used a code page called 862, while Greek users used 737. They were the same below 128 but different from 128 up, where all the funny letters resided. The national versions of MS-DOS had dozens of these code pages, handling everything from English to Icelandic and they even had a few “multilingual” code pages that could do Esperanto and Galician on the same computer! Wow! But getting, say, Hebrew and Greek on the same computer was a complete impossibility unless you wrote your own custom program that displayed everything using bitmapped graphics, because Hebrew and Greek required different code pages with different interpretations of the high numbers.

Meanwhile, in Asia, even more crazy things were going on to take into account the fact that Asian alphabets have thousands of letters, which were never going to fit into 8 bits. This was usually solved by the messy system called DBCS, the “double byte character set” in which some letters were stored in one byte and others took two. It was easy to move forward in a string, but dang near impossible to move backwards. Programmers were encouraged not to use s++ and s– to move backwards and forwards, but instead to call functions such as Windows’ AnsiNext and AnsiPrev which knew how to deal with the whole mess.

But still, most people just pretended that a byte was a character and a character was 8 bits and as long as you never moved a string from one computer to another, or spoke more than one language, it would sort of always work. But of course, as soon as the Internet happened, it became quite commonplace to move strings from one computer to another, and the whole mess came tumbling down. Luckily, Unicode had been invented.

Unicode

Unicode was a brave effort to create a single character set that included every reasonable writing system on the planet and some make-believe ones like Klingon, too. Some people are under the misconception that Unicode is simply a 16-bit code where each character takes 16 bits and therefore there are 65,536 possible characters. This is not, actually, correct. It is the single most common myth about Unicode, so if you thought that, don’t feel bad.

In fact, Unicode has a different way of thinking about characters, and you have to understand the Unicode way of thinking of things or nothing will make sense.

Until now, we’ve assumed that a letter maps to some bits which you can store on disk or in memory:

A -> 0100 0001

In Unicode, a letter maps to something called a code point which is still just a theoretical concept. How that code point is represented in memory or on disk is a whole nuther story.

In Unicode, the letter A is a platonic ideal. It’s just floating in heaven:

A

This platonic A is different than B, and different from a, but the same as A and A and A. The idea that A in a Times New Roman font is the same character as the A in a Helvetica font, but different from “a” in lower case, does not seem very controversial, but in some languages just figuring out what a letter is can cause controversy. Is the German letter ß a real letter or just a fancy way of writing ss? If a letter’s shape changes at the end of the word, is that a different letter? Hebrew says yes, Arabic says no. Anyway, the smart people at the Unicode consortium have been figuring this out for the last decade or so, accompanied by a great deal of highly political debate, and you don’t have to worry about it. They’ve figured it all out already.

Every platonic letter in every alphabet is assigned a magic number by the Unicode consortium which is written like this: U+0639.  This magic number is called a code point. The U+ means “Unicode” and the numbers are hexadecimal. U+0639 is the Arabic letter Ain. The English letter A would be U+0041. You can find them all using the charmap utility on Windows 2000/XP or visiting the Unicode web site.

There is no real limit on the number of letters that Unicode can define and in fact they have gone beyond 65,536 so not every unicode letter can really be squeezed into two bytes, but that was a myth anyway.

OK, so say we have a string:

Hello

which, in Unicode, corresponds to these five code points:

U+0048 U+0065 U+006C U+006C U+006F.

Just a bunch of code points. Numbers, really. We haven’t yet said anything about how to store this in memory or represent it in an email message.

Encodings

That’s where encodings come in.

The earliest idea for Unicode encoding, which led to the myth about the two bytes, was, hey, let’s just store those numbers in two bytes each. So Hello becomes

00 48 00 65 00 6C 00 6C 00 6F

Right? Not so fast! Couldn’t it also be:

48 00 65 00 6C 00 6C 00 6F 00 ?

Well, technically, yes, I do believe it could, and, in fact, early implementors wanted to be able to store their Unicode code points in high-endian or low-endian mode, whichever their particular CPU was fastest at, and lo, it was evening and it was morning and there were already two ways to store Unicode. So the people were forced to come up with the bizarre convention of storing a FE FF at the beginning of every Unicode string; this is called a Unicode Byte Order Mark and if you are swapping your high and low bytes it will look like a FF FE and the person reading your string will know that they have to swap every other byte. Phew. Not every Unicode string in the wild has a byte order mark at the beginning.



For a while it seemed like that might be good enough, but programmers were complaining. “Look at all those zeros!” they said, since they were Americans and they were looking at English text which rarely used code points above U+00FF. Also they were liberal hippies in California who wanted to conserve (sneer). If they were Texans they wouldn’t have minded guzzling twice the number of bytes. But those Californian wimps couldn’t bear the idea of doubling the amount of storage it took for strings, and anyway, there were already all these doggone documents out there using various ANSI and DBCS character sets and who’s going to convert them all? Moi? For this reason alone most people decided to ignore Unicode for several years and in the meantime things got worse.


***********:
Thus was invented the brilliant concept of UTF-8. UTF-8 was another system for storing your string of Unicode code points, those magic U+ numbers, in memory using 8 bit bytes. In UTF-8, every code point from 0-127 is stored in a single byte. Only code points 128 and above are stored using 2, 3, in fact, up to 6 bytes.



-------------
def valid_utf8(data):
    # Number of bytes remaining in the current UTF-8 character
    bytes_remaining = 0
    
    for num in data:
        # Convert the integer to a binary string of 8 bits
        bin_rep = format(num, '#010b')[-8:]

        if bytes_remaining == 0:
            # Determine the number of bytes in the UTF-8 character
            if bin_rep[0] == '0':
                continue  # 1-byte character
            elif bin_rep[:3] == '110':
                bytes_remaining = 1  # 2-byte character
            elif bin_rep[:4] == '1110':
                bytes_remaining = 2  # 3-byte character
            elif bin_rep[:5] == '11110':
                bytes_remaining = 3  # 4-byte character
            else:
                return False  # Invalid UTF-8 start byte
        else:
            # Continuation byte must start with '10'
            if bin_rep[:2] != '10':
                return False
            bytes_remaining -= 1

    # If we're expecting continuation bytes but didn't get them
    return bytes_remaining == 0

# Test the function with the provided list
print(valid_utf8([72, 101, 240, 159, 146, 150]))  # True

----------


Let's break down the line bin_rep = format(num, '#010b')[-8:] to understand how it works in detail.

1. format(num, '#010b')
This part of the code converts the integer num into a binary string with some specific formatting options:

format(num, 'b'):

This converts the integer num to its binary representation as a string.
For example, format(65, 'b') would give '1000001'.
# (in '#010b'):

This option tells format to include the '0b' prefix in the binary string.
The '0b' prefix indicates that the following string is a binary number.
For example, format(65, '#b') would give '0b1000001'.
010 (in '#010b'):

The 010 part specifies that the output string should be at least 10 characters long, including the '0b' prefix.
If the binary representation of num is shorter than 10 characters, it will be padded with leading zeros.
For example, format(65, '#010b') would give '0b01000001'.
2. [-8:]
This part of the code slices the binary string to extract only the last 8 bits:

[-8:]:
This slice extracts the last 8 characters from the binary string.
It effectively removes the '0b' prefix and ensures that the resulting bin_rep is an 8-bit binary number, which is what you need to represent a byte.
For example, given '0b01000001', slicing with [-8:] results in '01000001'.
Summary
Putting it all together:

format(num, '#010b') converts num to a 10-character string representing the binary value of num with a '0b' prefix and zero-padding if necessary.
[-8:] extracts the last 8 characters, resulting in the 8-bit binary representation of the number without the '0b' prefix.
Example:
For num = 65:

format(65, '#010b') results in '0b01000001'.
bin_rep = format(65, '#010b')[-8:] results in '01000001'.
This binary string '01000001' is then used for further processing, such as checking whether it matches the expected pattern in UTF-8 encoding.

---------
Valid Byte Check: By using format(i, '#010b')[-8:], you ensure that only the last 8 bits are considered. This correctly handles cases where integers exceed 255, as it strips the extra bits and focuses on the valid byte range.
