package Parser.MavenProject;

import junit.framework.TestCase;

public class test3 extends TestCase 
{
	public void test(){
		Parser p=new Parser();
		assertEquals("File Parsed","success",p.ParseRow("RowWiseTime.csv", 4));
	}
}
