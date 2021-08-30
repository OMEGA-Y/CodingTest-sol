import java.io.*;

public class remainder_10430 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] input = br.readLine().split(" ");
		int[] s = new int[input.length];
		
		int idx = 0;
		for(String token: input) {
			s[idx] = Integer.parseInt(token);
			idx++;
		}
		System.out.println((s[0]+s[1])%s[2]);
		System.out.println(((s[0]%s[2])+(s[1]%s[2]))%s[2]);
		System.out.println((s[0]*s[1])%s[2]);
		System.out.println(((s[0]%s[2])*(s[1]%s[2]))%s[2]);
	}
}
