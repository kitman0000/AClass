function setPageDivider()
		{  
			totalNumberOfPages = _totalNumberOfPages;
			
			var strHtml = "";
			
			var startPageNumber = 1;
			if(_currentPage > 10)
			{
				strHtml += "<li><a href='#' onClick='toFirstPage()' aria-label='Previous'><span aria-hidden='true'\"'><<</span> <span></span></a></li>";
				startPageNumber = Math.floor(_currentPage / 10) * 10;
				if(_currentPage % 10 != 0)
					startPageNumber++;
				else
				{
					startPageNumber -= 9;
				}
			}
			
			strHtml += "<li><a href='#' onClick='btnPrePageOnClick()' aria-label='Previous'><span aria-hidden='true'\"'>上一页</span> <span></span></a></li>";
			
			for(i = startPageNumber; i < startPageNumber + 10 && i <= totalNumberOfPages; i++) 
			{
				if(i == _currentPage)
				{
					strHtml += "<li class='active'><a href='#' onclick ='btnSwitchOnClick(" + i + ")'>" + i + "</a></li>";				 
				}
				else
				{
					strHtml += "<li><a href='#' onclick ='btnSwitchOnClick(" + i + ")'>" + i + "</a></li>";				 
				}
			}
			strHtml += "<li><a href='#' onClick='btnNextPageOnClick(" + totalNumberOfPages+ ")' aria-label='Previous'><span aria-hidden='true'>下一页</span> <span></span></a></li>";
			
			if(i - 1 != totalNumberOfPages)
			{
				strHtml += "<li><a href='#' onClick='toLastPage()' aria-label='Previous'><span aria-hidden='true'\"'>>></span> <span></span></a></li>";
			}
			$("#pageDivider").html(strHtml);
		}
		
		function toFirstPage()
		{
			_currentPage = 1;
			getItemInfoOfOnePage();
			setPageDivider();
		}
		
		function toLastPage()
		{
			_currentPage = _totalNumberOfPages;
			getItemInfoOfOnePage();
			setPageDivider();
		}
		
		function btnPrePageOnClick()
		{
			if(_currentPage > 1)
			{
				_currentPage--;
			
				getItemInfoOfOnePage();
				
				setPageDivider();
			}
			 
		}

		function btnSwitchOnClick(n)
		{
			_currentPage = n;
			getItemInfoOfOnePage();
			setPageDivider();
		}

		function btnNextPageOnClick(totalNumberOfPages)
		{
			if(_currentPage < totalNumberOfPages)
			{
				_currentPage++;
				getItemInfoOfOnePage();
				setPageDivider();
			}
		}