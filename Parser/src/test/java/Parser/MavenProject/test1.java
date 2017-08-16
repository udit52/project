package Parser.MavenProject;

import junit.framework.TestCase;
public class test1 extends TestCase 
{
	public void test()
	{
		Parser p=new Parser();
	//	System.out.println("Test Cases is being checked");
		assertEquals("File Parsed" , "success", p.ParseRow("RowWise.csv", 4));
	/*	assertEquals("Second.csv Parsed","success",p.ParseRow("Second.csv", 4));
		assertEquals("Third.csv Parsed","success",p.ParseRow("Third.csv", 4));
		assertEquals("Fourth.csv Parsed","success",p.ParseColumn("Fourth.csv", 4));
		assertEquals("Fifth.csv Parsed","success",p.ParseColumn("Fifth.csv", 4));
		assertEquals("Sixth.csv parsed Parsed","success",p.ParseColumn("Sixth.csv", 4));
		assertEquals("Seventh.csv Parsed","success",p.ParseColumn("Seventh.csv", 4));
	*/
	}
}
