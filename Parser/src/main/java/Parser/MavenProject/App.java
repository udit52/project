package Parser.MavenProject;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;


class DataPoint
{
	public String attributes[];
	int size;
	public DataPoint(int a)
	{
		size=a;
		attributes=new String[a];
		for(int i=0;i<a;++i)
		{
			attributes[i]="";
		}
	}
	
	public void show(int c)
	{
		int i,j;
		for(j=0;j<c;++j)
		{
			for(i=0;i<size;++i)
			{
				String[] temp=attributes[i].split(",");
				System.out.print(temp[j]+" ");
			}
			System.out.println();
		}
	}
}
// A Separate Parsing class for the CSV file which has 
// function to parse the file in which the user wants.
class Parser
{
	public String ParseRow(String f,int att) 
	{
		DataPoint dp=new DataPoint(att);
		BufferedReader br = null;
		String line = "";
		int c=0;
		try
		{
			br=new BufferedReader(new FileReader(f));
			while ((line = br.readLine()) != null) 
			{
					c++;
			        String cvsSplitBy = ",";
        	        String[] country = line.split(cvsSplitBy);
        			for(int i=0;i<country.length;++i)
					{
				//		System.out.println(country.length);
						dp.attributes[i]+=country[i]+",";
				//		System.out.print(country[i]+" ");
					}
			//		System.out.println();
			}
		//	dp.show(c);
		}
		catch (FileNotFoundException e) 
        {
            e.printStackTrace();
        }
        catch (IOException e)
        {
            e.printStackTrace();
        } 
        finally 
        {
            if (br != null) {
                try 
                {
                    br.close();
                } catch (IOException e)
                {
                    e.printStackTrace();
                }
            }
        }
		return "success";
	}
	
	public String ParseColumn(String f, int att)
	{
		DataPoint dp1=new DataPoint(att);
		BufferedReader br=null;
		String line="";
		String cvsSplitBy=",";
		int i=0,y=0,z=0;
		try
		{

		//	do
		//	{
				br=new BufferedReader(new FileReader(f));
				while((line=br.readLine())!=null)
				{
					String []country=line.split(cvsSplitBy);
					z=country.length;
					if(z==1)
					{
						y++;
						i=0;
						continue;
					}
		//			System.out.println(line);
		//			System.out.print(i+" ");
					dp1.attributes[i++]+=line+",n";
		//			System.out.println(dp1.attributes[i-1]);
		//			y=country.length;
				}
				String []country=dp1.attributes[i-1].split(cvsSplitBy);
		//		System.out.println();
		//	}while(x<y);
		//	dp1.show(country.length);
		}
		catch(FileNotFoundException e)
		{
			e.printStackTrace();
		}
		catch(IOException e)
		{
			e.printStackTrace();
		}
		finally
		{
			if(br!=null)
			{
				try
				{
					br.close();
				}
				catch(IOException e)
				{
					e.printStackTrace();
				}
			}
		}
		return "success";
	}
}
class ReadFile
{
    public static void main(String[] args) 
    {
    	Scanner sc=new Scanner(System.in);
	    String csvFile = "/Users/gopalji/Desktop/SampleTest/";
	    String f;
	    System.out.print("Enter File Name :");
	    f=sc.nextLine();
	    csvFile=csvFile+f;
	    System.out.println("Your File Address is :"+csvFile);
        String cvsSplitBy = ",";
		System.out.print("Is the data row wise(0) or column wise(1) {Enter 0 or 1} ?");
		int t=sc.nextInt();
		System.out.print("Enter total Attributes in the file :");
		int att=sc.nextInt();
		Parser p=new Parser();
		if(t==0)
			p.ParseRow(csvFile,att);
		else if(t==1)
			p.ParseColumn(csvFile,att);			
	}
}
/*  try {
			int c=0;
            br = new BufferedReader(new FileReader(csvFile));    
            while ((line = br.readLine()) != null) 
            {

                
                String[] country = line.split(cvsSplitBy);
                String[] type=new String[country.length];
                for(int i=0;i<type.length;++i)
                {
                	if(c==0)
					{
						type[i]=country[i].getClass().getName();
						System.out.print(type[i]);
					}
                }

				for(int i=0;i<country.length;++i)
				{
					
					System.out.print(country[i]+" ");
				}
				System.out.println();
				c++;

            }

        } 
        catch (FileNotFoundException e) 
        {
            e.printStackTrace();
        }
        catch (IOException e)
        {
            e.printStackTrace();
        } 
        finally 
        {
            if (br != null) {
                try 
                {
                    br.close();
                } catch (IOException e)
                {
                    e.printStackTrace();
                }
            }
        }
*/