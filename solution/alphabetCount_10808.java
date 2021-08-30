import java.io.*;

public class alphabetCount_10808 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String input = br.readLine();
		int[] list = new int[26];
		
		for(int i=0; i<input.length(); i++) {
			list[(int)input.charAt(i)-(int)'a']+=1;
		}
		
		for(int cnt: list) {
			System.out.print(cnt+" ");
		}
	}

}
