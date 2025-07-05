# Unicode Text Versus Bytes

## Character Issues


- Unicode: The abstract standard of characters called code points, a global language dictionary, to define word characters and give them a unique ID.
- UTF-*: Unicode Transformation Format
    - Converts Unicode code points into a stream of bytes readable by a computer.
    - Many different encode/decode formats.

- Encoding: Unicode Code Points --> Bytes
- Decoding: Bytes --> Unicode Code Points

![alt text](image.png)

## Byte Essentials

- Two Basic Built-in Binary Sequence Types:
    1. `bytes`: Immutable
    2. `bytearray`: Mutable

## Basic Encoders/Decoders

- Codec: Encoders/decoders
    - Named `utf-#`typically.

![alt text](image-1.png)

1. `latin1` *aka* `iso8859_1`: Important because it is the basis for other encodings, such as cp1252 and Unicode itself (note how the latin1 byte values appear in the cp1252 bytes and even in the code points).

2. `cp1252`: A useful latin1 superset created by Microsoft, adding useful symbols like curly quotes and € (euro); some Windows apps call it “ANSI,” but it was never a real ANSI standard.

3. `cp437`: The original character set of the IBM PC, with box drawing characters. Incompatible with latin1, which appeared later.

4. `gb2312`: Legacy standard to encode the simplified Chinese ideographs used in mainland China; one of several widely deployed multibyte encodings for Asian languages.

5. `utf-8`: The most common 8-bit encoding on the web, by far, as of July 2021.

6. `utf-16le`: One form of the UTF 16-bit encoding scheme; all UTF-16 encodings support code points beyond U+FFFF through escape sequences called “surrogate pairs.”

## Understanding Encode/Decode Problems

- `UnicodeEncodeError`: Error raised when converting `str` to binary sequences.
- `UnicodeDecodeError`: Error raised when reading binary sequences into `str`.
- `SyntaxError`: Error raised when the source encoding is unexpected when loading Python modules.


### Coping with UnicodeEncodeError

![alt text](image-2.png)
![alt text](image-3.png)

- `str.isascii()`: Method added in Python 3.7, returns a `bool` of whether your Unicode text is 100% pure ASCII or not.

### Coping with UnicodeDecodeError

![alt text](image-4.png)

### SyntaxError When Loading Modules with Unexpected Encoding

- `coding` comment: A comment at the top of a *.py* file indicating the codec used.

![alt text](image-5.png)

### How to Discover the Encoding of a Byte Sequence

### BOM: A Useful Gremlin

- BOM (Byte-order Mark): A special marker placed at the beginning of a text file that tells a computer how to read multi-byte characters. 

- Byte Order: 
    - Little-endian: The least important byte (smallest part) comes first.
    - Big-endian: The most important byte (biggest part) comes first.

- Because UTF-16 and UTF-32 use multiple bytes to store one character, the order matters. If two computers have different default byte orders, they might misread the characters unless there’s a BOM telling them what to expect.

- Example:
    - "E"
        - Unicode Code Point: U+0045
        - Hex: 0045
        - UTF-16be: 00 45 (big-endian)
        - UTF-16le: 45 00 (little-endian)

### Handling Text Files

- "Unicode Sandwich":
    - Bytes should be decoded as early as possible to `str` (top piece of bread).
    - Operations are performed on `str` (text) only (sandwich filling).
    - Finalized text is encoded on output (bottom piece of bread).

![alt text](image-6.png)


### Beware of Encoding Defaults

## Normalizing Unicode for Reliable Comparisions

- Canonical Equivalents: In Unicode, two different sequences of code points represent the same character or *visual appearance*, and are considered equal in meaning and form. BUT Python sees them as two **different** code points and considers them NOT equal.
    - Example: `é`& `e\u0301`
    - `unicodedata.normalize(arg1, arg2)`:
        - `arg1`: One of the following 4 strings:
            1. "NFC": Normalize Form C composes the code points to produce the shortest equivalent string.
            2. "NFD": Normalize Form D decomposes, expanding composed characters, into base characters and separate combining characters. 
            3. "NFKC":
            4. "NFKD":

![alt text](image-7.png)

### Case Folding

- Case Folding: Converting all text to lowercase and doing some additional transformations, supported by `str.casefold()`.

### Utility Functions for Normalized Text Matching

