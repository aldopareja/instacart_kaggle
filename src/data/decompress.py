import argparse, glob, os
import warnings as wr
import zipfile as zp

def main(inputDir,outputDir):
    inputFiles = glob.glob(os.path.join(inputDir,'*.zip'))
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
    else:
        wr.warn('the output directory already exists\n directory will be cleaned')
        out = glob.glob(os.path.join(outputDir,'*'))
        for file in out:
           os.remove(file)
    for file in inputFiles:
        file = zp.ZipFile(file, 'r')
        file.extractall(outputDir)
        file.close()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='script for decompressing the data files') 
    
    parser.add_argument('-i', '--input_directory', type=str,default=None ,help='The path to the input directory')
    parser.add_argument('-o', '--output_directory', type=str,default=None ,help='The output directory')

    '''
    python decompress.py -i data/raw/
                         -o data/raw/decompressed
    '''


    args = parser.parse_args()

    inputDir = args.input_directory
    outputDir = args.output_directory

    main(inputDir,outputDir)