import apache_beam as beam

# The DoFn to perform on each element in the input PCollection.
class Dummy(beam.DoFn):
    def process(self, element):
        return [element]

def run():
    p = beam.Pipeline('DirectRunner')
    (p | 'ReadMessage' >>  beam.io.textio.ReadFromTextWithFilename('inputs.txt')
                        | 'Processing' >> beam.ParDo(Dummy())
                        | 'Write' >> beam.io.WriteToText('results.txt'))
    result = p.run()
    result.wait_until_finish()

if __name__ == "__main__":
    run()