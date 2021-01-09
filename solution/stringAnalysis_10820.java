import java.io.*;
public class stringAnalysis_10820 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String input = "";
		while((input=br.readLine()) != null) {
			int[] cnt = new int[4];
			char[] chars = input.toCharArray();
			
			for(char c: chars) {
				if(Character.isLowerCase(c)) {
					cnt[0]+=1;
				}else if(Character.isUpperCase(c)) {
					cnt[1]+=1;
				}else if(Character.isDigit(c)) {
					cnt[2]+=1;
				}else {
					cnt[3]+=1;
				}
			}
			
			for(int i=0; i<cnt.length; i++) {
				if(i==cnt.length-1) {
					System.out.println(cnt[i]);
					break;
				}
				System.out.print(cnt[i]+" ");
			}
		}
		
		br.close();
	}

}
