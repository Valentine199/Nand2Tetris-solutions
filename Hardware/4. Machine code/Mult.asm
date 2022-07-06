// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

//we use a loop, to add R0 R1 times and store it in R2
//if there is anything in R2 we reset it to zero
@R2
M=0

(LOOP)
	//We check whether we need to do the opperation
	@R1
	D=M
	@END
	D;JLE
	
	//I store the value of R0
	@R0
	D=M
	@END
	D;JLE
	
	
	// I add it to R2
	@R2
	M = M + D
	
	//I subtract one from R1
	@R1
	M=M-1
	
@LOOP
0;JMP
	
(END)
@END
0;JMP
	