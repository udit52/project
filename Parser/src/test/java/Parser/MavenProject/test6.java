package Parser.MavenProject;

import junit.framework.TestCase;

public class test6 extends TestCase
{
	public void test(){
		Parser p=new Parser();
		assertEquals("File Parsed","success",p.ParseColumn("ColumnWiseTime.csv", 4));
	}
}
