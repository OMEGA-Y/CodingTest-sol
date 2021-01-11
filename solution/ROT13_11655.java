import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class ROT13_11655 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String input = br.readLine();
		char[] chars = input.toCharArray();
		
		int ord;
		for(char c : chars) {
			if(Character.isLowerCase(c)) {
				ord = 13+(int)c;
				if(ord>122) {
					ord -= 26;
				}
				System.out.print((char)ord);
			}
			else if(Character.isUpperCase(c)) {
				ord = 13+(int)c;
				if(ord>90) {
					ord -= 26;
				}
				System.out.print((char)ord);
			}
			else {
				System.out.print(c);
			}
		}
	}
}
