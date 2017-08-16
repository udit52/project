
package Parser.MavenProject;

import junit.framework.TestCase;

public class test4 extends TestCase 
{
	public void test(){
		Parser p=new Parser();
		assertEquals("File Parsed","success",p.ParseColumn("ColumnWise.csv", 4));
	}
}
