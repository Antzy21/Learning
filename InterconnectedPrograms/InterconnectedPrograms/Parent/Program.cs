// See https://aka.ms/new-console-template for more information
using System.Diagnostics;

Console.WriteLine("Hello, World!");

void recieveOutput(object sender, DataReceivedEventArgs data, StreamWriter streamWriter) {
    if (data.Data?.Contains("Readline") ?? false)
    {
        Console.WriteLine($"Child: " + data.Data);
        var line = Console.ReadLine();
        streamWriter.WriteLine(line);
    }
    else
    {
        Console.WriteLine($"Child: " + data.Data);
    }
}

using (var process = new Process())
{
    process.StartInfo.FileName = @"..\..\..\..\Child\bin\Debug\net6.0\Child.exe"; // relative path. absolute path works too.
    process.StartInfo.Arguments = $"";
    //process.StartInfo.FileName = @"cmd.exe";
    //process.StartInfo.Arguments = @"/c dir";      // print the current working directory information
    process.StartInfo.CreateNoWindow = true;
    process.StartInfo.UseShellExecute = false;

    process.StartInfo.RedirectStandardOutput = true;
    process.StartInfo.RedirectStandardError = true;
    process.StartInfo.RedirectStandardInput = true;

    Console.WriteLine("Starting");
    process.Start();

    var streamWriter = process.StandardInput;

    process.OutputDataReceived += (sender, data) => recieveOutput(sender, data, streamWriter);
    process.ErrorDataReceived += (sender, data) => Console.WriteLine($"{process.ProcessName}: " + data.Data);
    process.BeginOutputReadLine();
    process.BeginErrorReadLine();
    
    var exited = process.WaitForExit(1000 * 120);     // (optional) wait up to 120 seconds
    if (!exited)
    {
        Console.WriteLine("Killing Child");
        process.Kill();
    }
    else
    {
        Console.WriteLine("Child exited in time");
    }
}