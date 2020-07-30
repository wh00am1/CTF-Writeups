#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv){
	int var_ch = 0;
	while(1){
		if ((var_ch & 1) != 0 && ((var_ch & 0x100000) != 0 && (var_ch & 0x200) == 0)){
			printf("%d", var_ch);
			break;
		}
		else{
			var_ch = var_ch + 1;
		}
	}
}

