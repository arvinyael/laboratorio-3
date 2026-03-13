package Java;
import java.util.Scanner;
public class patitojv {

	public static void main(String[] args) {
		Scanner ls=new Scanner(System.in);
		int rango=ls.nextInt();
		for(int i=0;i<rango;i++) {
			int a=ls.nextInt();
			int b=ls.nextInt();
			if(a<b){
				System.out.println("<");
			}
			if(a>b){
				System.out.println(">");
			}
			if(a==b) {
				System.out.println("=");
			}
		}
	}

}
