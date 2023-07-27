; Remember This Tagets x64! 
    includelib kernel32.lib
    includelib msvcrt.lib
    GetStdHandle proto
    WriteFile proto
    ReadFile proto
    ExitProcess  proto
    .data
        
        hStdIn dq ?; stdin 
        hStdOut dq ?;stdout
        CellPointer qword 1000 dup(0)
    .code 
        main proc
            sub rsp, 28h        ; space for 4 arguments + 16byte aligned stack
        ;-------getting handles ---
        ;----stdin
        mov rcx, -11
        call GetStdHandle
        mov hStdOut, rax; DWORD hStdOut = GetStdHandle(-11);
        ;-----stdout
        mov rcx, -10
        call GetStdHandle
        mov hStdIn, rax;DWORD hStdIn = GetStdHandle(-10);
    
        add rsp, 28h
        ;-------end getting handles 
        mov rdx, offset CellPointer
        
    add qword ptr[RDX], 1; called by IncrementIt
    
    start_lblnum1: ; starting ----
    cmp qword ptr[RDX],0
    jz end_lblnum1
    ; scope start ----- 1
    
    sub qword ptr[RDX], 2;called by DeIncrementIt
    add RDX, 8
    
    sub qword ptr[RDX], 1;called by DeIncrementIt
    
    start_lblnum2: ; starting ----
    cmp qword ptr[RDX],0
    jz end_lblnum2
    ; scope start ----- 2
    add RDX, 16
    
    add qword ptr[RDX], 1; called by IncrementIt
    add RDX, 8
    
    sub qword ptr[RDX], 5;called by DeIncrementIt
    sub RDX, 16

    ;scope end ---- 2
    cmp qword ptr[RDX], 0
    jnz start_lblnum2
    end_lblnum2:; ending -----
    sub RDX, 8
    
    sub qword ptr[RDX], 2;called by DeIncrementIt
    sub RDX, 8
    
    sub qword ptr[RDX], 3;called by DeIncrementIt

    ;scope end ---- 1
    cmp qword ptr[RDX], 0
    jnz start_lblnum2
    end_lblnum1:; ending -----
    add RDX, 8
    
    sub qword ptr[RDX], 1;called by DeIncrementIt

    sub	rsp, 30h
	mov rcx, hStdOut
    push RDX
	mov rdx, offset CellPointer
	mov r8, 1
	call WriteFile
    pop RDX
	add rsp, 30h
        add RDX, 24
    
    add qword ptr[RDX], 1; called by IncrementIt

    sub	rsp, 30h
	mov rcx, hStdOut
    push RDX
	mov rdx, offset CellPointer
	mov r8, 1
	call WriteFile
    pop RDX
	add rsp, 30h
        add RDX, 16

    sub	rsp, 30h
	mov rcx, hStdOut
    push RDX
	mov rdx, offset CellPointer
	mov r8, 1
	call WriteFile
    pop RDX
	add rsp, 30h
    
    sub	rsp, 30h
	mov rcx, hStdOut
    push RDX
	mov rdx, offset CellPointer
	mov r8, 1
	call WriteFile
    pop RDX
	add rsp, 30h
        
    add qword ptr[RDX], 3; called by IncrementIt
    
    start_lblnum3: ; starting ----
    cmp qword ptr[RDX],0
    jz end_lblnum3
    ; scope start ----- 3

    sub	rsp, 30h
	mov rcx, hStdOut
    push RDX
	mov rdx, offset CellPointer
	mov r8, 1
	call WriteFile
    pop RDX
	add rsp, 30h
        add RDX, 8

    ;scope end ---- 3
    cmp qword ptr[RDX], 0
    jnz start_lblnum3
    end_lblnum3:; ending -----
    sub RDX, 32

    sub	rsp, 30h
	mov rcx, hStdOut
    push RDX
	mov rdx, offset CellPointer
	mov r8, 1
	call WriteFile
    pop RDX
	add rsp, 30h
        
    add qword ptr[RDX], 3; called by IncrementIt

    sub	rsp, 30h
	mov rcx, hStdOut
    push RDX
	mov rdx, offset CellPointer
	mov r8, 1
	call WriteFile
    pop RDX
	add rsp, 30h
        
    sub qword ptr[RDX], 6;called by DeIncrementIt

    sub	rsp, 30h
	mov rcx, hStdOut
    push RDX
	mov rdx, offset CellPointer
	mov r8, 1
	call WriteFile
    pop RDX
	add rsp, 30h
        sub RDX, 16
    
    sub qword ptr[RDX], 1;called by DeIncrementIt

    sub	rsp, 30h
	mov rcx, hStdOut
    push RDX
	mov rdx, offset CellPointer
	mov r8, 1
	call WriteFile
    pop RDX
	add rsp, 30h
        add RDX, 32
    
    add qword ptr[RDX], 1; called by IncrementIt

    sub	rsp, 30h
	mov rcx, hStdOut
    push RDX
	mov rdx, offset CellPointer
	mov r8, 1
	call WriteFile
    pop RDX
	add rsp, 30h
    main endp
end