# badserver
Buffer overflow exploit for Stephen Bradshaw's Vulnserver.

## Theory behind it
Programs have memory for it, they have a stack, heap, etc., etc.

![memory1](https://github.com/shodanwashere/badserver/blob/main/img1.png?raw=true)

Let’s focus on the Stack:

![memory2](https://github.com/shodanwashere/badserver/blob/main/img2.png?raw=true)

Buffer space grows downward. Normally we can write to the buffer space and it won’t be a problem because, if the program is written with proper memory management, the buffer can contain everything that is written to it:

![memory3](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/389ad78d-85b0-4009-bcfa-4d0bb0d3a8ea/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230102T152033Z&X-Amz-Expires=86400&X-Amz-Signature=dca76638889fc77864706dbb685a51c804be69dd59a75d9e437e0e9cc7ebacdc&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

Programs with improper memory management allow you to write to the buffer space as much as you want without keeping its contents contained, which means you can overwrite memory spaces below the buffer, like the EBP and the ******EIP******, which buffer overflow attacks target.

![memory4](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ee7b51f2-9688-40c3-af63-ab6ddb6b390c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230102T152057Z&X-Amz-Expires=86400&X-Amz-Signature=a69428500c628d2843a050880f606f32d2a842fc88b7748c30a8d3734219c1ea&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

The point of a buffer overflow attack is to overwrite the buffer space and the EBP with a bunch of garbage so we can reach the EIP, then overwrite that pointer with a memory address that points to a piece of code (for our purposes, malicious code).

For this exploit (which has a preconfigured payload, but this can be edited on code), we take advantage of an unsafe dynamic link library on vulnserver which has a `JMP ESP` instruction, which we can use to push the program execution to an address on the tip of our stack frame. The payload has, following the EIP address, a NOP sled and the payload shellcode, which means that, once the exploit is executed, the payload pushes the new return address into the EIP, which makes `JMP ESP` execute, which pushes program execution right on top of the NOP sled. The program execution then goes down the sled until it reaches the shellcode, and in principle, if your attacking machine is already listening for a communication on port 4444, you will have a reverse shell. Be mindful that the shellcode obtained was off of `msfvenom` with preconfigured parameters, so you'll have to generate your own shellcode if you want to use this exploit.
