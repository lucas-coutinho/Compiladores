

DIGITO	[0-9]
LETRA	[a-zA-Z]
ID	{LETRA}({LETRA}|_|{DIGITO})*	
BINARY  [&&|<|+|\-|*]  

COMMENT1 "//"(.)* 
COMMENT2 "/*"(.|\x)*"*/"
COMMENT ({COMMENT1}|{COMMENT2})
KEYWORDS ("class"|"public"|"static"|"void"|"main"|"String"|"return"|"boolean"|"int"|"if"|"else"|"while"|"System.out.println"|"true"|"false"|"this"|"new"|"!"|"extends"|"length"|"("|"["|"]"|"{"|"}"|")"|","|";"|"."|"=")

%%
{DIGITO}+		{printf("Inteiro_Literal: %s\n",yytext);} 
{KEYWORDS}    		{printf("Palavra reservada: %s\n", yytext);}
{ID}			{printf("var: %s\n",yytext);}
{BINARY}		{printf("binary operator: %s\n", yytext);}
{COMMENT}		{printf("Comentario: %s\n", yytext);}

%%
int yywrap();

main(){
  yylex();
}

int yywrap(){
 return 1;
}
