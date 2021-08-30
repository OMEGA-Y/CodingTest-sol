import java.io.*;
import java.util.Arrays;

public class alphabetFind_10809 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String input = br.readLine();
		
		int[] list = new int[26];
		Arrays.fill(list, -1);
		
		for(int i=0; i<input.length(); i++) {
			int ord = input.charAt(i)-97;
			if(list[ord] == -1) {
				list[ord] = i;
			}
		}
		
		for(int i:list) {
			System.out.print(i+" ");
		}
		
		br.close();
	}
}
