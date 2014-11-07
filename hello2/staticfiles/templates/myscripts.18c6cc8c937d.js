$(document).ready(function() {
   
//	Initiliaze the table
	var table = $('#example').DataTable();
//  Function to get the new row selected.
	function fnGetSelected(table) {
		return table.$('tr.row_selected');
	}
	/* Add a click handler to the rows - this could be used as a callback */
	$('#example tbody tr').click(e){
		if($(this).hasClass('row_selected')){
		   $(this).removeClass('row_selected')
		}
		else{
			
		}
	}
	
	$('#addRow').on( 'click', function () {
        t.row.add( [
            '.1',
            '.2',
            '.3',
            '.4',
            '.5'
        ] ).draw();
    } );
 
 
    function fnGetSelected(table){
    	return table.$(table).
    }

   


} );		
