package Parser.MavenProject;

import junit.framework.TestCase;

public class test7 extends TestCase 
{
	public void test(){
		Parser p=new Parser();
		assertEquals("Seventh.csv Parsed","success",p.ParseColumn("Seventh.csv", 4));
	}
}
