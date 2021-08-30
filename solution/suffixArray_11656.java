import java.io.*;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class suffixArray_11656 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String input = br.readLine();
		List<String> suffix = new ArrayList<>();
		
		for(int i=0; i<input.length(); i++) {
			suffix.add(input.substring(i));
		}
		
		Collections.sort(suffix);
		
		for(String s : suffix) {
			System.out.println(s);
		}
		
		br.close();
	}
}
