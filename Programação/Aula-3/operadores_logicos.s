	.file	"operadores_logicos.c"
	.text
	.section .rdata,"dr"
.LC0:
	.ascii "%d\12\0"
.LC1:
	.ascii "%d %d\12\0"
	.text
	.globl	main
	.def	main;	.scl	2;	.type	32;	.endef
	.seh_proc	main
main:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$64, %rsp
	.seh_stackalloc	64
	.seh_endprologue
	call	__main
	movl	$5, -4(%rbp)
	movl	$3, -8(%rbp)
	movl	-4(%rbp), %eax
	andl	-8(%rbp), %eax
	movl	%eax, -12(%rbp)
	movl	-12(%rbp), %eax
	leaq	.LC0(%rip), %rcx
	movl	%eax, %edx
	call	printf
	movl	-4(%rbp), %eax
	orl	-8(%rbp), %eax
	movl	%eax, -16(%rbp)
	movl	-16(%rbp), %eax
	leaq	.LC0(%rip), %rcx
	movl	%eax, %edx
	call	printf
	movl	-4(%rbp), %eax
	xorl	-8(%rbp), %eax
	movl	%eax, -20(%rbp)
	movl	-20(%rbp), %eax
	leaq	.LC0(%rip), %rcx
	movl	%eax, %edx
	call	printf
	movl	-4(%rbp), %eax
	notl	%eax
	movl	%eax, -24(%rbp)
	movl	-24(%rbp), %eax
	leaq	.LC0(%rip), %rcx
	movl	%eax, %edx
	call	printf
	movl	-4(%rbp), %eax
	sarl	%eax
	movl	%eax, -28(%rbp)
	movl	-4(%rbp), %eax
	addl	%eax, %eax
	movl	%eax, -32(%rbp)
	movl	-32(%rbp), %edx
	movl	-28(%rbp), %eax
	leaq	.LC1(%rip), %rcx
	movl	%edx, %r8d
	movl	%eax, %edx
	call	printf
	movl	$0, %eax
	addq	$64, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.def	__main;	.scl	2;	.type	32;	.endef
	.ident	"GCC: (Rev3, Built by MSYS2 project) 16.2.0"
	.def	printf;	.scl	2;	.type	32;	.endef
