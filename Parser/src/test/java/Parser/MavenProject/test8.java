package Parser.MavenProject;

import junit.framework.TestCase;

public class test8 extends TestCase {
	public void test()
	{
		Parser p=new Parser();
		assertEquals("File Parsed","success",p.ParseRow("RowWiseDeviceSeries.csv",4));
	}

}
