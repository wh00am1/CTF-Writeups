#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv){
	int var_14 = 0;
	while(1){
		if ((var_14 & 1) != 0 && ((var_14 & 0x100000) != 0 && (var_14 & 0x200) == 0)){
			printf("%d", var_14);
			break;
		}
		else{
			var_14 = var_14 + 1;
		}
	}
}

