package Parser.MavenProject;

import junit.framework.TestCase;

public class test5 extends TestCase 
{
	public void test(){
		Parser p=new Parser();
		assertEquals("File Parsed","success",p.ParseColumn("ColumnWiseDevice.csv", 4));
	}
}
