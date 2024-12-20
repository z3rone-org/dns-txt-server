from dnslib import DNSRecord, RR, QTYPE, TXT
from dnslib.server import DNSServer
import os

class FileBasedTXTResolver:
    def __init__(self, data_directory):
        """
        Initialize the resolver with the directory containing TXT record files.
        :param data_directory: Path to the directory where files are stored.
        """
        self.data_directory = data_directory

    def resolve(self, request, handler):
        """
        Resolve DNS TXT queries using file-based responses.
        :param request: The DNS request object.
        :param handler: The handler (not used here but part of the interface).
        :return: A DNSRecord containing the answer or an empty response.
        """
        reply = request.reply()
        question = request.questions[0]
        qname = str(question.qname).rstrip('.').lower()
        qtype = QTYPE[question.qtype]

        if qtype == "TXT":
            file_path = os.path.join(self.data_directory, qname)
            if os.path.exists(file_path) and os.path.isfile(file_path):
                with open(file_path, 'r') as f:
                    txt_data = f.read().strip()
                reply.add_answer(RR(qname, QTYPE.TXT, rdata=TXT(txt_data)))
            else:
                # If the file does not exist, return an empty reply
                print(f"No TXT file found for query: {qname}")
        else:
            print(f"Unsupported query type: {qtype}")

        return reply

def run_dns_server(data_directory, address='0.0.0.0', port=53):
    """
    Run a DNS server with the file-based TXT resolver.
    :param data_directory: Path to the directory containing TXT record files.
    :param address: The address to bind the server to.
    :param port: The port to bind the server to.
    """
    resolver = FileBasedTXTResolver(data_directory)
    server = DNSServer(resolver, address=address, port=port)
    print(f"Starting DNS server on {address}:{port}, serving TXT records from {data_directory}")
    server.start()

if __name__ == "__main__":
    # Start the DNS server
    run_dns_server(
        data_directory=os.environ.get('RECORD_DIR', './dns_txt_records'),
        address=os.environ.get('LISTEN_IP', '0.0.0.0'),
        port=int(os.environ.get('LISTEN_PORT', '53'))
    )

