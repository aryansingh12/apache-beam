import apache_beam as beam, re
with beam.Pipeline() as p:
    (p
    | beam.io.ReadFromText("count.txt")
    | beam.FlatMap(lambda a:re.split("\\W+", s))
    | beam.combiners().Count.PerElement()
    | beam.Map(lambda w,c: "%s: %d" %(w,c))
    | beam.io.textio.WriteToText("output/stringscounts")
    )


# read from text
# flat map to convert it into 
# combiners - group by and then counting
# map for formatting
# S3, gcs, or any other file thing