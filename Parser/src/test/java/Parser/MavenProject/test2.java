package Parser.MavenProject;

import junit.framework.TestCase;

public class test2 extends TestCase
{
	public void test()
	{
		Parser p=new Parser();
		assertEquals("File Parsed","success",p.ParseRow("RowWiseDevice.csv", 4));
	}
}
