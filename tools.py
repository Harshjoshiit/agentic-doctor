import os
from dotenv import load_dotenv
load_dotenv()

from crewai_tools import BaseTool
from crewai_tools.tools.serper_dev_tool import SerperDevTool
from langchain.document_loaders import PDFLoader  # Added missing import

# Creating search tool
search_tool = SerperDevTool()

# Creating custom pdf reader tool
class BloodTestReportTool():
    async def read_data_tool(self, path='data/sample.pdf'):  # Added self parameter
        """Tool to read data from a pdf file from a path

        Args:
            path (str, optional): Path of the pdf file. Defaults to 'data/sample.pdf'.

        Returns:
            str: Full Blood Test report file
        """
        
        docs = PDFLoader(file_path=path).load()

        full_report = ""
        for data in docs:
            # Clean and format the report data
            content = data.page_content
            
            # Remove extra whitespaces and format properly
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")
                
            full_report += content + "\n"
            
        return full_report

# Creating Nutrition Analysis Tool
class NutritionTool:
    async def analyze_nutrition_tool(self, blood_report_data):  # Added self parameter
        # Process and analyze the blood report data
        processed_data = blood_report_data
        
        # Clean up the data format
        i = 0
        while i < len(processed_data):
            if processed_data[i:i+2] == "  ":  # Remove double spaces
                processed_data = processed_data[:i] + processed_data[i+1:]
            else:
                i += 1
                
        # TODO: Implement nutrition analysis logic here
        return "Nutrition analysis functionality to be implemented"

# Creating Exercise Planning Tool
class ExerciseTool:
    async def create_exercise_plan_tool(self, blood_report_data):  # Added self parameter
        # TODO: Implement exercise planning logic here
        return "Exercise planning functionality to be implemented"