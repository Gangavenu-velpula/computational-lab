inputfile ='/home/r210785/Downloads/Chorus.wav';
outputFile = '/home/r210785/Videos/venu/venu.wav';
% Read the audio file
[y, Fs]= audioread(inputfile);
% Reverse the sample order
reversedData = flipud(y);
% Save the reversed audio to a new file
audiowrite(outputFile, reversedData, Fs);

disp('Audio file reversed and saved successfully!');
