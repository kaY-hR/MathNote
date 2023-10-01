using System;
using System.IO;
using System.Text;
using System.Linq;
using System.Collections.Generic;
using System.Xml;

class Program
{
    static string GetLabelsFromMd(string mdFile)
    {
        foreach (var line in File.ReadLines(mdFile, Encoding.UTF8))
        {
            if (line.StartsWith("#"))
            {
                return line.TrimStart('#').Trim();
            }
        }
        return string.Empty;
    }

    static void Main()
    {
        // 書き換える本体のhtmlファイル名
        string targetHtml = "0_Main.html";

        // 同一フォルダにあるmdファイル名を取得
        var mdFilesList = Directory.EnumerateFiles(".", "*.md").OrderBy(f => f).ToList();
        mdFilesList.Remove(".\\README.md");

        // リスト内の各mdファイル名と同一のhtmlファイル名を生成
        var htmlFilesList = mdFilesList.Select(md => Path.ChangeExtension(md, ".html")).ToList();
        
        // mdFilesListの各mdファイルを開いて、labelsListを生成
        var labelsList = new List<string>();
        foreach (var mdFile in mdFilesList)
        {
            try
            {
                string label = GetLabelsFromMd(mdFile);
                labelsList.Add(label);
            }
            catch (Exception)
            {
                continue;
            }
        }

        // tabsDataを生成
        var tabsData = new List<dynamic>();
        for (int i = 0; i < htmlFilesList.Count; i++)
        {
            var tabData = new
            {
                id = Path.GetFileNameWithoutExtension(htmlFilesList[i]),
                label = labelsList[i],
                file = htmlFilesList[i].Substring(2)
            };
            tabsData.Add(tabData);
        }

        // 本体のhtmlファイルを読み込み、該当の部分にtabsDataを差し替え
        string content = File.ReadAllText(targetHtml, Encoding.UTF8);

        // 置換
        string startMarker = "// AutomaticallyReplace-start";
        string endMarker = "// AutomaticallyReplace-end";
        int startIndex = content.IndexOf(startMarker);
        int endIndex = content.IndexOf(endMarker) + endMarker.Length;

        List<string> tabsDataStrList = new List<string>();
        foreach (var tab in tabsData)
        {
            string tabDataStr = string.Format("\t\t\t\t{{ id: '{0}', label: '{1}', file: '{2}' }}", tab.id, tab.label, tab.file);
            tabsDataStrList.Add(tabDataStr);
        }

        string tabsDataStr = string.Join(",\n", tabsDataStrList);
        string newContent = content.Substring(0, startIndex) + startMarker + "\n" + tabsDataStr + "\n\t\t\t\t" + endMarker + content.Substring(endIndex);

        // 本体のhtmlファイルを上書き保存
        File.WriteAllText(targetHtml, newContent, Encoding.UTF8);
    }
}
